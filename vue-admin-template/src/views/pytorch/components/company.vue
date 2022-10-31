<template>
  <div>
    <!-- <table /> -->
    <svg width="332" height="330" id="svgHTML" />
  </div>
</template>
<script>
import * as d3 from 'd3'
const format = d3.format(',d')
let current_circle = undefined
export default {
  name: 'App',
  props: {
    DataSource: {
      type: String, //表示是star issue 还是
      default: '0'
    }
  },
  data() {
    return {
      // data是getdata()的返回结果
      data_as_array: [],
      // data_as_json是异步的，所以需要在mounted()中赋值
      data_as_json: {},
      svg: undefined
    }
  },
  mounted() {
    this.BuildNameHeader()
    this.CreateBubbleChart()
    this.DrawCircle()
  },
  methods: {
    // async 函数getdata()，用于获取数据

    async BuildNameHeader() {
      const data_as_text = await d3.text('/dev-api/api/issue')
      this.data_as_array = d3.csvParseRows(data_as_text)
      // 如果DataSource为0，表示是star
      // if (this.DataSource === 0) {
      //   // 获取star数据
      //   const data_as_text = await d3.text('/dev-api/api/star_gazer')
      //   this.data_as_array = d3.csvParseRows(data_as_text)
      // } else if (this.DataSource === 1) {
      //   // 获取issue数据
      //   const data_as_text = await d3.text('/dev-api/api/issue')
      //   this.data_as_array = d3.csvParseRows(data_as_text)
      //   // 将数据转换为数组
      // } else if (this.DataSource === 2) {
      //   // 获取pull request数据
      //   const data_as_text = await d3.text('/dev-api/api/committer')
      //   this.data_as_array = d3.csvParseRows(data_as_text)
      // }
      // table为<table></table>
      console.log('ttttttttttttttttttttttttttttttt')
      const table = <table></table>

      const tableObject = d3.select(table)
      tableObject
        .append('tr') // 1. Append a <tr> element to the table
        .selectAll('th') // 2. Select all <th> elements in the <tr> (there are none)
        .data(this.data_as_array[0]) // 3. "Join" that selection to the first row in the CSV data we recieved (an array of string column headers)
        .enter() // 4. Perform another selection - getting all elements that do not exist in the table header yet
        .append('th') // 5. Take this selection (which is all the elements) and append a <th> element
        .text(d => d)
      tableObject
        .selectAll('tr')
        .data(this.data_as_array.slice(1, 15)) // Join the table rows to the rows in the CSV file (now a js array)
        .enter()
        .append('tr')
        .selectAll('td')
        .data(d => d) // Join the table values to the table data
        .enter()
        .append('td')
        .text(d => d)
    },
    flatNodeHeirarchy() {
      const root = { children: this.data_as_json } // remove the first value from the dataset - which is an aggregate we don't need
      return d3.hierarchy(root).sum(d => d.count)
    },
    packedData() {
      const width = 570
      const height = 570

      const pack = d3.pack().size([width, height]).padding(3)

      return pack(this.flatNodeHeirarchy())
    },
    async CreateBubbleChart() {
      // 初始化a的类型为Array
      this.data_as_json = await d3.csv(this.DataSource)

      const width = 930
      const height = 930
      const pack = d3.pack().size([width, height]).padding(3)

      return pack(this.flatNodeHeirarchy())
    },
    async DrawCircle() {
      this.data_as_json = await d3.csv(this.DataSource)

      this.svg = d3
        .select('body')
        .select('#svgHTML')
        .style('width', '100%')
        .style('height', 'auto')
        .attr('font-size', 10)
        .attr('font-family', 'sans-serif')
        .attr('text-anchor', 'middle')
      const leaf = this.svg
        .selectAll('g')
        .data(this.packedData().leaves())
        .enter()
        .append('g')
        .attr('transform', d => `translate(${d.x + 1},${d.y + 1})`)

      const circle = leaf
        .append('circle')
        .attr('r', d => d.r)
        .attr('fill', d => '#aaccff')
        .on('click', function (d) {
          if (this.current_circle !== undefined) {
            this.current_circle.attr('fill', d => '#bbccff')
            this.svg.selectAll('#details-popup').remove()
          }

          // select the circle
          current_circle = d3.select(this)
          current_circle.attr('fill', '#b2e1f9')

          const textblock = this.svg
            .selectAll('#details-popup')
            .data([d])
            .enter()
            .append('g')
            .attr('id', 'details-popup')
            .attr('font-size', 14)
            .attr('font-family', 'sans-serif')
            .attr('text-anchor', 'start')
            .attr('transform', d => `translate(0, 20)`)
          // 原来之前的text是用来这个用处的 ，还得加回来
          console.log('hhh')
          textblock.append('text').text('Occupation Details:').attr('font-weight', 'bold')
          textblock
            .append('text')
            .text(d => 'Description: ' + d.data.Occupation_Name)
            .attr('y', '16')
          textblock
            .append('text')
            .text(d => 'Current Employment: ' + format(d.data.Employment))
            .attr('y', '32')
          textblock
            .append('text')
            .text(d => 'Projected Growth: ' + format(d.data.Employment_Growth))
            .attr('y', '48')
          textblock
            .append('text')
            .text(d => 'Recent Labour Market Conditions: ' + d.data.Recent_Labour_Market_Conditions.toUpperCase())
            .attr('y', '64')
          textblock
            .append('text')
            .text(
              d => 'Projected Future Labour Market Conditionsh: ' + d.data.Future_Labour_Market_Conditions.toUpperCase()
            )
            .attr('y', '80')
        })
      const label = leaf
        .append('text')
        .attr('dy', '0.3em')
        .text(d => d.data.company)
        .attr('font-size', d => d.r / 4)
        .attr('color', 'black')
      console.log('label', label)
    }
  }
  //   buildnameheader
}
</script>

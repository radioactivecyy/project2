<template>
  <div>
    <!-- <table /> -->
    <!-- <按钮 -->
    
    <svg width="332" height="330" id="svgHTML_committer"  />
  </div>
</template>
<script>
import * as d3 from 'd3'

const format = d3.format(',d')
let current_circle = undefined
export default {
  name: 'App',
  props: {
 
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
      const data_as_text = await d3.text('/dev-api/api/pytorch_committer')
      this.data_as_array = d3.csvParseRows(data_as_text)
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
      this.data_as_json = await d3.csv('/dev-api/api/pytorch_committer')
     
      const width = 930
      const height = 930
      const pack = d3.pack().size([width, height]).padding(3)

      return pack(this.flatNodeHeirarchy())
    },
    async DrawCircle() {
      this.data_as_json = await d3.csv('/dev-api/api/pytorch_committer')
      this.svg = d3
        .select('body')
        .select('#svgHTML_committer')
        .style('width', '100%')
        .style('height', 'auto')
        .attr('font-size', 10)
        .attr('font-family', 'sans-serif')
        .attr('text-anchor', 'middle')
        const Mysvg = this.svg
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
        .on('mouseover', function (d) {
          if (current_circle !== undefined) {
            current_circle.attr('fill', d => '#aaccff')
            Mysvg.selectAll('#details-popup').remove()
            leaf.selectAll('text').remove()
          }
          current_circle = d3.select(this)
          current_circle.attr('fill', '#b2e1f9')
          const thisr = current_circle.attr('r')
          let labelx = 0
          let labely = 0
          let iii
          circle.each(function (d, i) {
            const thisr_num = Number(thisr)
            const s = d.r === thisr_num
            console.log('thisr', thisr_num, 'typetr', typeof thisr_num, 'same', s)
            if (d.r === thisr_num) {
              labelx = d.x
              labely = d.y
              iii = i
              console.log('IIIII', i)
            }
          })
          console.log('iii', iii)
          const showlabel = leaf
            .append('text')
            .attr('dy', '1.3em')
            .text(function (d, i) {
              if (iii === i) {
                return d.data.count
              }
            })
            .attr('font-size', d => d.r / 4)
            .attr('color', 'black')
          const label = leaf
            .append('text')
            .attr('dy', '0.3em')
            .text(d => d.data.company)
            .attr('font-size', d => d.r / 4)
            .attr('color', 'black')
        
        }).on('mouseout', function (d) {
          if (current_circle !== undefined) {
            current_circle.attr('fill', d => '#aaccff')
            leaf.selectAll('text').remove()
          }
          console.log('current_circle', current_circle)
          // 删除原有文字重新渲染
          leaf.selectAll('text').remove()
          const label = leaf
            .append('text')
            .attr('dy', '0.3em')
            .text(d => d.data.company)
            .attr('font-size', d => d.r / 4)
            .attr('color', 'black')
        })
      const label = leaf
        .append('text')
        .attr('dy', '0.3em')
        .text(d => d.data.company)
        .attr('font-size', d => d.r / 4)
        .attr('color', 'black')
    }
  }
  //   buildnameheader
}
</script>

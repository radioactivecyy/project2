<template>
  <div>
    <!-- <table /> -->
    <!-- <按钮 -->
    <svg width="332" height="330" id="svgHTML_c" />
  </div>
</template>
<script>
import * as d3 from 'd3'
const format = d3.format(',d')
let current_circle = undefined
export default {
  name: 'App',
  props: {},
  data() {
    return {
      // data是getdata()的返回结果
      data_as_array: [],
      // data_as_json是异步的，所以需要在mounted()中赋值
      data_as_json: {},
      svg: undefined,
      data_pytorch,
      pandas_num
    }
  },
  mounted() {
    // this.BuildNameHeader()
    this.CreateBubbleChart()
    this.DrawCircle()
  },
  methods: {
    // async 函数getdata()，用于获取数据
    async BuildNameHeader() {
      const data_as_text = await d3.text('/dev-api/api/issue')
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
      this.data_as_json = await d3.csv('/dev-api/api/committer')
      const width = 930
      const height = 930
      const pack = d3.pack().size([width, height]).padding(3)

      return pack(this.flatNodeHeirarchy())
    },
    async DrawCircle() {
      this.data_as_json = await d3.csv('/dev-api/api/committer')
      // 给每条数据添加一个属性 asize

      // console.log('this.data_as_json111', this.data_as_json)
      // 遍历data_as_json,如果有company出现两次，就把两个company的isRepeat都设置为1
      for (var i = 0; i < this.data_as_json.length; i++) {
        for (var j = i + 1; j < this.data_as_json.length; j++) {
          if (this.data_as_json[i].company === this.data_as_json[j].company) {
            this.data_as_json[i].isRepeat = '1'
            this.data_as_json[j].isRepeat = '1'
          }
        }
      }
      // 把数组按照count大小排序，并且不改变原数组的大小

      for (var i = 0; i < this.data_as_json.length; i++) {
        for (var j = i + 1; j < this.data_as_json.length; j++) {
          if (this.data_as_json[i].count < this.data_as_json[j].count) {
            var temp = this.data_as_json[i]
            this.data_as_json[i] = this.data_as_json[j]
            this.data_as_json[j] = temp
          }
        }
      }

      this.svg = d3
        .select('body')
        .select('#svgHTML_c')
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
        // 根据下标判断是否是pytorch的数据，是的话就用红色，否则用蓝色
        .attr('fill', (d, i) => {
          //  console.log('d',d)
          if (d.data.flag === '0') {
            return '#aaccff'
          } else {
            return '#ff8a8a'
          }
        })
        // 在圆圈外面加一个白色的圆圈 使得圆圈更加醒目
        // 圆圈的半径是原来的1.2倍
        .attr('stroke', (d,i)=>{
          if (d.data.duplicate === '0') {
            
          } else {
            if(d.data.flag === '0'){
              return '#80bfff'
          }else{
            return '99ccff'
          }
          }
        })
      
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

    }
  }
  //   buildnameheader
}
</script>

<!-- d3js 气泡图 -->
<template>
  <div id="bubble" style="width: 500px; height: 500px"></div>
</template>

<script>
import * as echarts from 'echarts'
import * as d3 from 'd3'
require('echarts/theme/macarons') // echarts theme
import resize from '../mixins/resize'
var ROOT_PATH = 'https://echarts.apache.org/examples'

var chartDom = document.getElementById('main')
var myChart = echarts.init(chartDom)
var option
export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '400px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart(seriesData, maxDepth) {
      var data = [4, 8, 15, 16, 23, 42]

      var x = d3.scale
        .linear()
        .domain([0, d3.max(data)])
        .range([0, 420])

      var tooltip = d3
        .select('body')
        .append('div')
        .style('position', 'absolute')
        .style('z-index', '10')
        .style('visibility', 'hidden')
        .style('background', '#000')
        .text('a simple tooltip')

      d3.select('body')
        .selectAll('div')
        .data(data)
        .enter()
        .append('div')
        .style('width', function (d) {
          return x(d) + 'px'
        })
        .text(function (d) {
          return d
        })
        .on('mouseover', function (d) {
          tooltip.text(d)
          return tooltip.style('visibility', 'visible')
        })
        .on('mousemove', function () {
          return tooltip.style('top', d3.event.pageY - 10 + 'px').style('left', d3.event.pageX + 10 + 'px')
        })
        .on('mouseout', function () {
          return tooltip.style('visibility', 'hidden')
        })
    }
  }
}
</script>

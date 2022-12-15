<template>

  <div class="chart-wrapper" :style="{ height: height, width: width }" />
</template>
<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from '../mixins/resize'
export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '110%'
    },
    height: {
      type: String,
      default: '260px'
    },
    autoResize: {
      type: Boolean,
      default: true
    },
    MyTitle:{
      type: String,
      default: ''
    },
    // chartData: {
    //   type: ,
    //   required: true
    // },
   
    Year: {
      type: String,
      default: '2017'
    },
    MyTitle:{
      type: String,
      default: ''
    }
  },

  data() {
    return {
      chart: null
    }
  },
  
  watch: {
    // watch Year if it changes, then update the chart
    Year:{
      handler: function (val) {
      
        this.chart.setOption({
          series: [{
            data: this.getVirtualData(this.Year)
          }],
          calendar: [{
            // top: 20,
            // left: 'center',
            
            range: this.Year
          }]

        })
      },
      deep: true,
      immediate: true
    }
   
  },
  // 新建mounted 否则会出现init没有定义
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
    // 初始化图表
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      this.setOptions()
    },
    getVirtualData(year) {

      const date = +echarts.number.parseDate(year + '-01-01')
      const end = +echarts.number.parseDate(+year + 1 + '-01-01')

      const dayTime = 3600 * 24 * 1000
      const data = []
      for (let time = date; time < end; time += dayTime) {
        data.push([echarts.format.formatTime('yyyy-MM-dd', time), Math.floor(Math.random() * 2000)])
      }
     
      return data
    },
    // 设置图表数据
    setOptions({ expectedData, actualData } = {}) {
      this.chart.setOption({
        title: {
          top: 30,
          left: 'center',
          text: this.MyTitle
        },
        tooltip: {},
        visualMap: {
          min: 0,
          max: 2000,
          type: 'piecewise',
          orient: 'horizontal',
          left: 'center',
          top: 65,
          // inRange: {
          //   color: ['#d94e5d', '#eac736', '#50a3ba'].reverse()
          // }
        },
        calendar: {
          top: 120,
          left: 30,
          right: 30,
          cellSize: ['auto', 13],
          range: this.Year,
          itemStyle: {
            borderWidth: 0.5
          },
          yearLabel: { show: false }
        },
        series: {
          type: 'heatmap',
          coordinateSystem: 'calendar',
          data: this.getVirtualData(this.Year)
        }
      })
    }
  }
}
</script>
<style>
.chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
  </style>
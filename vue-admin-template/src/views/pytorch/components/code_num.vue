<template>
  <div :class="className" :style="{ height: height, width: width }" />
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
      default: '100%'
    },
    height: {
      type: String,
      default: '400px'
    },
    chartData:{
      type: Object,
      required: true
    },
    myTitle:{
      type: String,
      required: true,
      default: '贡献者'
    }

  },
  data() {
    return {
      chart: null,
      msg: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.initChart(val)
      }
    },

  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      setTimeout(() => {
        var mydata = JSON.parse(JSON.stringify(this.chartData))
        console.log('mydata',mydata)
        // 遍历数据，
        var mysource=[]
        var mysource1=mydata.x
        var mysource2=mydata.y1
        var mysource3=mydata.y2
        // 将mysource1添加到mysource中
        mysource.push(mysource1)
        // 将mysource2添加到mysource中
        mysource.push(mysource2)
        // 将mysource3添加到mysource中
        mysource.push(mysource3)
      console.log('mysource',mysource)
        var option = {
          legend: {
            orient: 'vertical',
            right: 10,
            top: 20,
            bottom: 20
          },
          tooltip: {
            trigger: 'axis',
            showContent: false,
            dataZoom: {
              type: 'inside'
            }
          },
          dataset: {

            source: mysource
          },
          title: {
            // 位置设置为底部

            left: 'center',
            text: this.myTitle
          },
          dataZoom: {
            type: 'slider',
            start: 0,
            end: 100
          },
          xAxis: { type: 'category' },
          yAxis: { gridIndex: 0 },
          grid: { top: '55%' },
          series: [
            {
              type: 'line',
              smooth: true,
              seriesLayoutBy: 'row',
              emphasis: { focus: 'series' }
            },
            {
              type: 'line',
              smooth: true,
              seriesLayoutBy: 'row',
              emphasis: { focus: 'series' }
            },

            {
              type: 'pie',
              id: 'pie',
              radius: '30%',
              center: ['50%', '25%'],
              emphasis: {
                focus: 'self'
              },
              label: {
                formatter: '{b}: {@[' + 1 + ']} ({d}%)'
              },
              encode: {
                itemName: 0,
                value: 1,
                tooltip: 1
              }
            }
          ]
        }
        const C = this.chart
        const T = this
        this.chart.on('updateAxisPointer', function (event) {
          const xAxisInfo = event.axesInfo[0]
          if (xAxisInfo) {
            T.msg = xAxisInfo.value
            T.$emit('func', T.msg)
            const dimension = xAxisInfo.value + 1
            console.log('dimension',dimension)
            C.setOption({
              series: {
                id: 'pie',
                label: {
                  formatter: '{b}: {@[' + dimension + ']} ({d}%)'
                },
                encode: {
                  value: dimension,
                  tooltip: dimension
                }
              }
            })
          }
        })
        this.chart.setOption(option)
      }, 1000)
    }
  }
}
</script>

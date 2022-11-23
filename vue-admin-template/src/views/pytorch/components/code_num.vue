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
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      setTimeout(() => {
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
            source: [
              ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
              ['核心贡献者', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
              ['其余贡献者', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
           
            ]
          },
          title: {
            // 位置设置为底部

            left: 'center',
            text: '贡献者'
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
                formatter: '{b}: {@2012} ({d}%)'
              },
              encode: {
                itemName: 'product',
                value: '2012',
                tooltip: '2012'
              }
            }
          ]
        }
        console.log('chart', this.chart)
        let C = this.chart
        this.chart.on('updateAxisPointer', function (event) {
          const xAxisInfo = event.axesInfo[0]
          console.log('hhdh', C)
          if (xAxisInfo) {
            const dimension = xAxisInfo.value + 1
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

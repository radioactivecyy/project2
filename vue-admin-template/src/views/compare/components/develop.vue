<template>
  <div>
    <div id="main1" :style="{ height: height, width: 400 }" />
    <div id="main2" :style="{ height: height, width: 400 }" />
  </div>
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
// import resize from '../mixins/resize'

export default {
  //   mixins: [resize],
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
      default: '350px'
    },
    // autoResize: {
    //   type: Boolean,
    //   default: true
    // },
    // chartData: {
    //   type: Object,
    //   required: true
    // }
  },
  data() {
    return {
      chart1: null,
      chart2: null
    }
  },
  watch: {
    // chartData: {
    //   deep: true,
    //   handler(val) {
    //     this.setOptions(val)
    //   }
    // }
  },
  // 新建mounted 否则会出现init没有定义
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart1) {
      return
    }
    if (!this.chart2) {
      return
    }
    this.chart1.dispose()
    this.chart2.dispose()
    this.chart1 = null
    this.chart2 = null
  },
  methods: {
    // 初始化图表
    initChart() {
      // 设置两个chart 不重复
      this.chart1 = echarts.init(document.getElementById('main1'), 'macarons')

      console.log('chart1')
      this.chart2 = echarts.init(document.getElementById('main2'), 'macarons')

      var option1 = {
        // 指定第1个图表的配置项和数据
        color: ['LimeGreen', 'DarkGreen', 'red', 'blue', 'Purple'],
        toolbox: {
          show: true,
          feature: {
            dataZoom: {
              xAxisIndex: 'none'
            }
          }
        },
        dataZoom: {
          show: true,
          realtime: true,
          start: 0,
          end: 100
        },
        backgroundColor: 'rgba(128, 128, 128, 0.1)', //rgba设置透明度0.1
        title: { text: '某学院2019年专业招生情况汇总表', left: 40, top: 5 },
        tooltip: { tooltip: { show: true } },
        legend: { data: ['2019年招生'], left: 422, top: 8 },
        xAxis: [
          {
            data: ['大数据', '云计算', 'Oracle', 'ERP', '人工智能', '软件开发', '移动开发', '网络技术'],
            axisLabel: { interval: 0 }
          }
        ],
        yAxis: [{ type: 'value' }],
        series: [
          {
            //配置第1个图表的数据系列
            name: '2019年招生',
            type: 'bar',
            barWidth: 40, //设置柱状图中每个柱子的宽度
            data: [125, 62, 45, 56, 123, 205, 108, 128]
          }
        ]
      }
      // 基于准备好的dom,初始化ECharts图表
      //   this.chart2 = echarts.init(document.getElementById('main2'))
      var option2 = {
        // 指定第2个图表的配置项和数据
        color: ['blue', 'LimeGreen', 'DarkGreen', 'red', 'Purple'],
        toolbox: {
          show: true,
          feature: {
            dataZoom: {
              xAxisIndex: 'none'
            }
          }
        },
        dataZoom: {
          show: false,
          realtime: true,
          start: 0,
          end: 100
        },
        backgroundColor: 'rgba(128, 128, 128, 0.1)', // rgba设置透明度0.1
        title: { text: '某学院2020年专业招生情况汇总表', left: 40, top: 8 },
        tooltip: { show: true },
        legend: { data: ['2020年招生'], left: 422, top: 8 },
        xAxis: [
          {
            data: ['大数据', '云计算', 'Oracle', 'ERP', '人工智能', '软件开发', '移动开发', '网络技术'],
            axisLabel: { interval: 0 }
          }
        ],
        yAxis: [{ type: 'value' }],
        series: [
          {
            // 配置第2个图表的数据系列
            name: '2020年招生',
            type: 'bar',
            barWidth: 40, // 设置柱状图中每个柱子的宽度
            data: [325, 98, 53, 48, 222, 256, 123, 111]
          }
        ]
      }
      console.log('hhh')
      console.log('this.chart1', this.chart1)
      console.log('this.chart2', this.chart2)
      this.chart1.setOption(option1) // 为myChart1对象加载数据
      this.chart2.setOption(option2) // 为myChart2对象加载数据
      // 多图表联动配置方法1：分别设置每个echarts对象的group值
      this.chart1.group = 'group1'
      this.chart2.group = 'group1'
      echarts.connect('group1')
    }

    // }
  }
}
</script>

<template>
  <div :class="className" :style="{ height: height, width: width }" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from '../mixins/resize'
// 导入词云
import 'echarts-wordcloud'
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
      default: '350px'
    },
    autoResize: {
      type: Boolean,
      default: true
    },
    chartData: {
      type: Object,
      required: true
    },
    Mytitle: {
      type: String,
      required: true
    },
    dataSource: {
      type: String,
      required: true
    },
    color1: {
      type: String,
      required: true
    },
    color2: {
      type: String,
      required: true
    },
    color3: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      chart: null,
      mydata: {}
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
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
      console.log('cloud inittttttttttttttttttttttttt')
      this.setOptions(this.chartData)
    },
    // 设置图表数据
    setOptions({ expectedData, actualData } = {}) {
    //   var mydata = JSON.parse(JSON.stringify(this.chartData))

    //   this.date = mydata.x

    //   this.data = mydata.y
      this.chart.setOption({
        series: [
          {
            type: 'wordCloud',
            /*
        绘制词云的形状, 值为回调函数 或 关键字, 默认 circle
        关键字:
        circle  圆形
        cardioid 心形
        diamond  菱形 正方形
        triangle-forward, triangle  三角形  
        pentagon 五边形
        star 星形
        */
            shape: 'circle',

            // The shape option will continue to apply as the shape of the cloud to grow.
            //词云轮廓图，支持为 HTMLImageElement, HTMLCanvasElement，不支持路径字符串, 不包含白色区域; 可选选项
            // shape选项将随着云的形状增长而继续应用。
            //maskImage: maskImage,

            // 词云整个图表放置的位置 和 尺寸大小
            left: 'center',
            top: 'center',
            width: '70%',
            height: '80%',
            right: null,
            bottom: null,

            //词云文本大小范围,  默认为最小12像素，最大60像素。
            sizeRange: [12, 60],

            // 词云文字旋转范围和步长。 文本将通过旋转在[-90，90]范围内随机旋转步骤45
            // 如果都设置为 0 , 则是水平显示
            rotationRange: [-90, 90],
            rotationStep: 45,

            // 词云文本之间的距离, 距离越大，单词之间的间距越大, 单位像素
            gridSize: 8,

            //设置为true可以使单词部分在画布之外绘制, 允许绘制大于画布大小的单词
            drawOutOfBound: false,

            // 文本样式
            textStyle: {
              normal: {
                fontFamily: 'sans-serif',
                fontWeight: 'bold',
                // 回调函数 或 颜色值
                color: function () {
                  // 默认 随机颜色
                  return (
                    'rgb(' +
                    [
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160)
                    ].join(',') +
                    ')'
                  )
                }
              },
              // 鼠标hover的特效样式
              emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
              }
            },

            // data 数组格式, 必须有name和value属性,
            data: [
              {
                name: 'Farrah Abraham',
                value: 366,
                // 单独设置文本颜色
                textStyle: {
                  color: this.createRandomItemStyle()
                }
              },
              {
                name: 'b Abraham',
                value: 122,
                // 单独设置文本颜色
                textStyle: {
                  color: this.createRandomItemStyle()
                }
              },
              {
                name: 'aa Abraham',
                value: 40,
                // 单独设置文本颜色
                textStyle: {
                  color: this.createRandomItemStyle()
                }
              },
              {
                name: 'ddd Abraham',
                value: 200,
                // 单独设置文本颜色
                textStyle: {
                  color: this.createRandomItemStyle()
                }
              }
            ]
          }
        ]
      })
    },
    // 生成随机颜色
    createRandomItemStyle() {
      return (
        'rgb(' +
        [Math.round(Math.random() * 180), Math.round(Math.random() * 360), Math.round(Math.random() * 360)].join(',') +
        ')'
      )
    }
  }
}
</script>

<template>
  <div>
    <svg width="332" height="330" id="legend_s" />
  </div>
</template>
<script>
import * as d3 from 'd3'
export default {
  data() {
    return {
      svg: undefined,
      data: []
    }
  },
  mounted() {
    this.createlegend()
  },
  methods: {
    createlegend() {
     var ldata = [
        {
          name: 'A',
          color: '#4a9b5b'
        },
        {
          name: 'B',
          color: '#5caeb9'
        },
        {
          name: 'C',
          color: '#df4b4b'
        },
        {
          name: 'D',
          color: '#cb7e51'
        },
        {
          name: 'E',
          color: '#1942f4'
        }
      ]
        this.svg = d3.select('body')
        .select('#legend_s')
        .style('width', '100%')
        .style('height', 'auto')
        .attr('font-size', 10)
        .attr('font-family', 'sans-serif')
        .attr('text-anchor', 'middle')
      var legend = this.svg
      d3Legend.legendColor()
  .shape("path", d3.symbol().type(d3.symbolTriangle).size(150)())
  // Try commenting shapePadding() to see the difference
  .shapePadding(25) // cell padding
  .labelOffset(20)  // label offset from the shape
  .scale(scale)
    }
  }
}
</script>

<template>
  <div>
    <h2>Legend</h2>
    Click on the legend elements
    <ul class="removeBulletAddTick">
      <li v-for="(input, index) in legend_class" :key="`input-${index}`">
        <div class="legendElementWrapper" @click="sendFilterInput(input, index)">
          <svg width="20" height="20">
            <rect :style="cssRectFill(input)" width="20" height="20" />
          </svg>
          {{ input }}
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
// import * as d3 from "d3";

export default {
  name: 'Leg',
  props: {
    data: Array,
    colorScale: null
  },
  data: function() {
    return {
      legend_class: [],
      clickInput: []
    }
  },
  created: function() {
    this.legend_class = this.data
      .map(a => a.Genre)
      .filter((x, i, a) => a.indexOf(x) == i)
      .sort(function(a, b) {
        return parseFloat(a) - parseFloat(b)
      })
    this.clickInput = new Array(this.legend_class.length).fill(false)
  },
  mounted: function() {},
  methods: {
    sendFilterInput(input, index) {
      if (this.clickInput[index] == false) {
        this.clickInput[index] = true
        this.$emit('inputChange', input)
      } else if (this.clickInput[index] == true) {
        this.clickInput[index] = false
        this.$emit('inputChangeBack', input)
      }
    },
    cssRectFill(legItem) {
      return {
        '--fill': this.colorScale(legItem)
      }
    }
  },
  computed: {}
}
</script>

<style>
ul {
  text-align: left;
}
.legendElementWrapper {
  cursor: pointer;
}
rect {
  fill: var(--fill);
}
</style>

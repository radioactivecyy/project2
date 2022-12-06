// svg 保存成Png  fuction
export default {
  svgToPng(svg, pngWidth, pngHeight) {
    var serializer = new XMLSerializer()
    var source = '<?xml version="1.0" standalone="no"?>\r\n' + serializer.serializeToString(svg.node())
    var image = new Image()
    image.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(source)
    var canvas = document.createElement('canvas')
    canvas.width = pngWidth
    canvas.height = pngHeight
    var context = canvas.getContext('2d')
    context.fillStyle = '#fff' // 设置保存后的PNG 是白色的
    context.fillRect(0, 0, 10000, 10000)
    context.drawImage(image, 0, 0)
    return canvas.toDataURL('image/png')
  }
}

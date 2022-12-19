import request from '../utils/request'

export function getStar() {
  return request({
    url: 'api/issue',
    method: 'get'
  })
}

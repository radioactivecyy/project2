import request from '../utils/request'
export function searchRepo() {
  return request({
    url: 'api/test/',
    method: 'get'
  })
}

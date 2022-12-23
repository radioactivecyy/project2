import request from '../utils/request'

export function refreshData() {
  return request({
    url: 'api/update_pytorch',
    method: 'get'
  })
}

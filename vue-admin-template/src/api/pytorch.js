import request from '../utils/request'

export function refreshData() {
  return request({
    url: 'api/test_update',
    method: 'get'
  })
}

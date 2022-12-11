import request from '../utils/request'
export function getIssueDevelop() {
  return request({
    url: 'api/issuedev',
    method: 'get'
  })
}
export function getStarDevelop() {
  return request({
    url: 'api/stardev',
    method: 'get'
  })
}
export function getCommitDevelop() {
  return request({
    url: 'api/commitdev',
    method: 'get'
  })
}
export function getInsDel(startindex, endindex) {
  return request({
    url: 'api/insdel',
    method: 'get',
    // 参数：start end
    // 如果都是-1的话，就是全部
    params: {
      start: startindex,
      end: endindex
    }
  })
}
export function getContribution() {
  return request({
    url: 'api/contribution',
    method: 'get'
  })
}
// post
export function getContributionCloud(index) {
  return request({
    url: 'api/contributionCloud',
    method: 'get',
    params: {
      index: index
    }
  })
}
export function getDesign() {
  return request({
    url: 'api/design',
    method: 'get'
  })
}
export function getDesignCloud() {
  return request({
    url: 'api/designcloud',
    method: 'get'
  })
}
export function OgetIssueDevelop() {
  return request({
    url: 'api/issuedev',
    method: 'get'
  })
}
export function OgetStarDevelop() {
  return request({
    url: 'api/stardev',
    method: 'get'
  })
}
export function OgetCommitDevelop() {
  return request({
    url: 'api/commitdev',
    method: 'get'
  })
}
export function OgetInsDel(startindex, endindex) {
  return request({
    url: 'api/insdel',
    method: 'get',
    // 参数：start end
    // 如果都是-1的话，就是全部
    params: {
      start: startindex,
      end: endindex
    }
  })
}
export function OgetContribution() {
  return request({
    url: 'api/contribution',
    method: 'get'
  })
}
// post
export function OgetContributionCloud(index) {
  return request({
    url: 'api/contributionCloud',
    method: 'get',
    params: {
      index: index
    }
  })
}
export function OgetDesign() {
  return request({
    url: 'api/design',
    method: 'get'
  })
}
export function OgetDesignCloud() {
  return request({
    url: 'api/designcloud',
    method: 'get'
  })
}

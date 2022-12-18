import request from '../utils/request'
export function getIssueDevelop() {
  return request({
    url: 'api/issuedev',
    method: 'get'
  })
}
export function PgetContributionDesign() {
  return request({
    url: 'api/compound_pie_design',
    method: 'get'
  })
}

export function PgetContributionFile() {
  return request({
    url: 'api/compound_pie_file',
    method: 'get'
  })
}

export function getYearCommit(year) {
  return request({
    url: 'api/commit_year',
    method: 'get',
    params: {
      year: year
    }
  })
}
export function getStar() {
  return request({
    // headers: {
    //   Accept: 'application/vnd.github.v3.star+json'
    // },
    url: 'https://api.github.com/repos/pytorch/pytorch/stargazers',
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
export function PgetContribution() {
  return request({
    url: 'api/compound_pie_commit',
    method: 'get'
  })
}
export function getContribution() {
  return request({
    url: 'api/comp_commit',
    method: 'get'
  })
}
export function OgetContributionDesign() {
  return request({
    url: 'api/comp_design',
    method: 'get'
  })
}
export function OgetContributionFile() {
  return request({
    url: 'api/comp_file',
    method: 'get'
  })
}

// post
export function getContributionCloud() {
  return request({
    url: 'api/contributor_wordcloud',
    method: 'get'
  })
}
export function getDesign() {
  return request({
    url: 'api/desi_week',
    method: 'get'
  })
}
export function getDesignCloud() {
  return request({
    url: 'api/intro_wordcloud',
    method: 'get'
  })
}
export function OgetIssueDevelop() {
  return request({
    url: 'api/issue_both',
    method: 'get'
  })
}
export function OgetStarDevelop() {
  return request({
    url: 'api/star_both',
    method: 'get'
  })
}
export function OgetCommitDevelop() {
  return request({
    url: 'api/commit_both',
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
export function getInsDelbyHour() {
  return request({
    url: 'api/modi_hour',
    method: 'get'
  })
}
export function OgetInsDelbyHour() {
  return request({
    url: 'api/pandas_modi_hour',
    method: 'get'
  })
}
export function OgetContribution() {
  return request({
    url: 'api/comp_commit',
    method: 'get'
  })
}

export function OgetDesign() {
  return request({
    url: 'api/comp_design_b',
    method: 'get'
  })
}
export function OgetDesignCloud() {
  return request({
    url: 'api/p_introcloud',
    method: 'get'
  })
}

export function refreshOther() {
  return request({
    url: 'api/test1',
    method: 'get'
  })
}

export function getContribCloudP(index) {
  return request({
    url: 'api/contribcloudp',
    method: 'get',
    params: {
      index: index
    }
  })
}
export function getContribCloudO() {
  return request({
    url: 'api/pandas_contricloud',
    method: 'get'
  })
}

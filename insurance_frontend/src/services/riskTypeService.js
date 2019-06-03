import api from './api';

export default {
  getRiskTypes () {
    return api.execute('get', '/risk_types/')
  },
  getRiskType (id) {
      return api.execute('get', `/risk_types/${id}/`)
  },
  createRiskType (data) {
      return api.execute('post', '/risk_types/', data)
  },
  // updateRiskType (id, data) {
  //     return api.execute('put', `/risk_types/${id}`, data)
  // },
  // deleteRiskType (id) {
  //     return api.execute('delete', `/risk_types/${id}`)
  // }

}
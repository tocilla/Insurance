import api from './api';

export default {
  getRisks () {
      return api.execute('get', '/risks/')
  },
  getRisk (id) {
      return api.execute('get', `/risks/${id}/`)
  },
  createRisk (data) {
      return api.execute('post', '/risks/', data)
  },
  updateRisk (id, data) {
      return api.execute('put', `/risks/${id}/`, data)
  },
  deleteRisk (id) {
      return api.execute('delete', `/risks/${id}/`)
  }

}
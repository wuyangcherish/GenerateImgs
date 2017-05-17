import axios from 'axios'

axios.defaults.baseURL = "http://127.0.0.1:1024"
axios.defaults.headers.common['Content-Type'] = 'application/json'

const searchApi = {
	searchPerson(person) {
		let apiUrl = '/search';
		return axios.get(apiUrl, {
			params: {
				"person": person
			}
		})
	}
}

export default searchApi
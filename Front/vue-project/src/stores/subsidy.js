import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useAccountStore } from './account';

export const UseSubsidyStore = defineStore('Subsidy', () => {
    const subsidies = ref('')
    const API_URL =  'http://127.0.0.1:8000'
    
    
    const getSubsidies = function () {
        const storeAccount = useAccountStore()
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/subsidies/`,
            headers : {
                Authorization: `Token ${storeAccount.token}`
            }
        })
        .then( res => {
            console.log(res)
            // console.log('dd')
            console.log(res.data)
            subsidies.value = res.data.results
            console.log('subsidies.value',subsidies.value)
        })
        .catch(err => console.log(err))
    }
    
  return { getSubsidies, subsidies, API_URL
   }
}, { persist: true })

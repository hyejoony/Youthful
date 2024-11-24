import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useAccountStore } from './account';

export const UseSavingStore = defineStore('Saving', () => {
    const savings = ref([])
    const API_URL =  'http://127.0.0.1:8000'
    
    const getSavings = function () {
        const storeAccount = useAccountStore()
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/savings/`,
            headers : {
                Authorization: `Token ${storeAccount.token}`
            }
        })
        .then( res => {
            console.log(res)
            // console.log('dd')
            console.log(res.data)
            savings.value = res.data.results
            console.log('savings.value',subsidies.value)
        })
        .catch(err => console.log(err))
    }

    
  return { getSavings, savings, API_URL
   }
}, { persist: true })

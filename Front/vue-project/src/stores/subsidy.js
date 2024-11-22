import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router';

export const UseSubsidyStore = defineStore('Subsidy', () => {
    const subsidies = ref([])
    const API_URL =  'http://127.0.0.1:8000'
    
    const getSubsidies = function () {
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/subsidies/`
        })
        .then( res => {
            console.log(res)
            console.log('dd')
            subsidies.value = res.data
        })
        .catch(err => console.log(err))
    }
    
  return { getSubsidies
   }
}, { persist: true })

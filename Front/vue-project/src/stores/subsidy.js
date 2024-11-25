import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useAccountStore } from './account';

export const UseSubsidyStore = defineStore('Subsidy', () => {
    const subsidies = ref([])
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
            subsidies.value = res.data.results
        })
        .catch(err => console.log(err))
    }
    
    const recoSubsidies = ref([])
    
    const getRecoSubsidies = function () {
        const storeAccount = useAccountStore()
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/subsidies/recommend/`,
            headers : {
                Authorization: `Token ${storeAccount.token}`
            }
        })
        .then( res => {
            console.log('과연!!!!!!!', res.data)
            recoSubsidies.value = res.data
        })
        .catch(err => console.log(err))
    }
  return { getSubsidies, subsidies, API_URL, getRecoSubsidies, recoSubsidies
   }
}, { persist: true })

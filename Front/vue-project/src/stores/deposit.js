import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useAccountStore } from './account';

export const UseDepositStore = defineStore('Deposit', () => {
    const deposits = ref([])
    const API_URL =  'http://127.0.0.1:8000'
    
    const getDeposits = function () {
        const storeAccount = useAccountStore()
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/deposits/`,
            headers : {
                Authorization: `Token ${storeAccount.token}`
            }
        })
        .then( res => {
            deposits.value = res.data.results
        })
        .catch(err => console.log(err))
    }

    const recoDeposits = ref([])

    const getRecoDeposits = function () {
        const storeAccount = useAccountStore()
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/deposits/recommend/`,
            headers : {
                Authorization: `Token ${storeAccount.token}`
            }
        })
        .then( res => {
            console.log('과연!!!!!!!', res.data)
            recoDeposits.value = res.data
        })
        .catch(err => console.log(err))
    }

    
  return { getDeposits, deposits, API_URL, getRecoDeposits, recoDeposits
   }
}, { persist: true })

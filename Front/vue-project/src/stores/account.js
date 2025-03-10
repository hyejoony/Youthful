import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router';

export const useAccountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  const emailErr = ref('')
  const password1Err = ref('')
  const password2Err = ref('')
  const birthyearErr = ref('')
  const incomeErr = ref('')
  const regionErr = ref('')
  const careerErr = ref('')
  const sameErr = ref('')



  const signUp = (payload) => {
    const email = payload.email

    const formData = new FormData();
    formData.append('email', payload.email);
    formData.append('nickname', payload.nickname);
    formData.append('password1', payload.password1);
    formData.append('password2', payload.password2);
    formData.append('birthyear', payload.birthyear);
    formData.append('income', payload.income);
    formData.append('career', payload.career);
    formData.append('region', payload.region);
    formData.append('condition1', payload.condition1);
    formData.append('condition2', payload.condition2);


    // profile_image가 File 객체인 경우
    if (payload.profile_image instanceof File) {
      formData.append('profile_image', payload.profile_image, payload.profile_image.name);
    }

    axios({
      method: 'post',
      url: `${API_URL}/accounts/dj-rest-auth/registration/`,
      data: formData
    })
      .then(res => {
        clearErrors()
        console.log('회원가입이 완료되었습니다.')
        const password = payload.password1
        logIn({ email, password })
        // console.log('dfdfdfdf')
        router.push({name: 'home'})
      })
      .catch(err => {
        console.log('회원가입 실패')
        const detail = err.response?.data?.detail || {};
  
        emailErr.value = detail.email?.[0] ?? '';
        password1Err.value = detail.password1?.[0] ?? '';
        password2Err.value = detail.non_field_errors?.[0] ?? '';
        birthyearErr.value = detail.birthyear?.[0] ?? '';
      // income, region, career에 대한 오류 처리
      if (detail.income?.[0] === '"null" is not a valid choice.') {
        incomeErr.value = '필수입니다';
      } else {
        incomeErr.value = detail.income?.[0] ?? '';
      }

      if (detail.region?.[0] === '"null" is not a valid choice.') {
        regionErr.value = '필수입니다';
      } else {
        regionErr.value = detail.region?.[0] ?? '';
      }

      if (detail.career?.[0] === '"null" is not a valid choice.') {
        careerErr.value = '필수입니다';
      } else {
        careerErr.value = detail.career?.[0] ?? '';
      }

      if (err.response.data.detail === '회원가입 처리 중 오류가 발생했습니다.') {
        sameErr.value = '이미 존재하는 회원입니다';
      }
        // console.log(err.response.data)
      })
  }

  const clearErrors = () => {
    emailErr.value = ''
    password1Err.value = ''
    password2Err.value = ''
    birthyearErr.value = ''
    incomeErr.value = ''
    regionErr.value = ''
    careerErr.value = ''
    sameErr.value = ''
  }

  const loginErr = ref('')
  const token = ref(null)
  const userId = ref(null)
  const userImage = ref(null)
  const userEmail = ref('')
  const userName = ref('')
  const userCareer = ref('')
  const userRegion = ref('')
  const userIncome = ref('')
  const userBirthyear = ref('')

  const logIn = (payload) => {
    const formData = new FormData();
    formData.append('email', payload.email);
    formData.append('password', payload.password);

    axios({
        method: 'post',
        url: `${API_URL}/accounts/dj-rest-auth/login/`,
        data: formData
    })
    .then(res => {
        loginErr.value = '';
        console.log('로그인이 완료되었습니다.');
        token.value = res.data.key;
        console.log(token.value)

        // 로그인 후 사용자 정보 가져오기
        return axios.get(`${API_URL}/accounts/user/`, {
            headers: {
                Authorization: `Token ${token.value}`
            }
        });
    })
    .then(userRes => {
        // 사용자 정보 저장
        console.log(userRes.data)
        userId.value = userRes.data.id;  // userId는 반응형 변수라고 가정
        userImage.value = userRes.data.profile_image
        userEmail.value = userRes.data.email
        userName.value = userRes.data.user_display_name
        userCareer.value = userRes.data.career
        userRegion.value = userRes.data.region
        userIncome.value = userRes.data.income
        userBirthyear.value = userRes.data.birthyear
        
        console.log(userId.value)
        console.log(userImage.value)
        router.push({ name: 'home' });
    })
    .catch(err => {
        loginErr.value = '잘못 입력하셨습니다.';
        console.log(err.response.data.non_field_errors ? err.response.data.non_field_errors[0] : err.message);
    });
  };

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const logout = () => {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/dj-rest-auth/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
    }
    })
    .then(res => {
      console.log('로그아웃 되었습니다')
      token.value = null
      router.push({ name: 'home' })
    })
    .catch(err => {
      console.log(token.value)
      console.log(err.response.data)
    })
  }

  // 데이터 저장
  const saveUpdateChanges = (payload) => {
    console.log('과연', payload)
    const id = payload.id
    const formData = new FormData()
    formData.append('nickname', payload.editNickname);
    formData.append('income', payload.editIncome);
    formData.append('career', payload.editCareer);
    formData.append('region', payload.editregion);

    // profile_image가 File 객체인 경우
    if (payload.editProfileImage instanceof File) {
      formData.append('profile_image', payload.editProfileImage, payload.editProfileImage.name);
    }

    return axios({
      method: 'put',
      url: `${API_URL}/accounts/profile/${id}/`,
      headers: {
        Authorization: `Token ${token.value}`,
        'Content-Type': 'multipart/form-data'
      },
      data: formData
    })
    .then(res => {
      console.log('수정 완료')
      return res.data
    })
    .catch(err => {
      console.log(err.response.data)
      return false
    })
  }


  return { signUp, API_URL, emailErr, password1Err, password2Err, birthyearErr,
    incomeErr, regionErr, careerErr, sameErr, clearErrors, logIn, loginErr,
    token, isLogin, userId, logout, saveUpdateChanges, userImage, userEmail, 
    userName, userCareer, userRegion, userIncome, userBirthyear
   }
}, { persist: true })

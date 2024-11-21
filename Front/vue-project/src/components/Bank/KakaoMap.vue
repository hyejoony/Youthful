<template>
    <div>
        <div id="map" style="width: 100%; height: 400px;"></div>
        <ul id="placesList"></ul>
        <div id="pagination"></div>
    </div>
</template>

<script setup>
import { ref, onMounted, defineProps, watch } from 'vue';

const props = defineProps({
    searchParams: {
        type: Object,
        required: true
    }
})

const markers = ref([])
let map // map 객체
let infowindow //팝업 정보
let keyword = ref('')

const searchPlaces = (searchKeyword) => {
    const ps = new kakao.maps.services.Places()
    ps.keywordSearch(searchKeyword, placesSearchCB)
}

const placesSearchCB = (data, status) => {
    if (status === kakao.maps.services.Status.OK) {
        // 기존 마커들을 모두 제거
        removeAllMarkers()

        const bounds = new kakao.maps.LatLngBounds()

        for (let i = 0; i < data.length; i++) {
            displayMarker(data[i])
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x))
        }

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        map.setBounds(bounds)
    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert('검색 결과가 존재하지 않습니다.')
    } else if (status === kakao.maps.services.Status.ERROR) {
        alert('검색 결과 중 오류가 발생했습니다.')
    }
}

const displayMarker = (place) => {
    const marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x),
    })

    // 마커에 클릭 이벤트 등록
    kakao.maps.event.addListener(marker, 'click', () => {
        infowindow.setContent(`<div style="padding:5px;font-size:12px;">${place.place_name}</div>`)
        infowindow.open(map, marker)
    })

    markers.value.push(marker) // 생성된 마커를 배열에 추가
}

// 모든 마커를 제거하는 함수
const removeAllMarkers = () => {
    for (let i = 0; i < markers.value.length; i++) {
        markers.value[i].setMap(null);
    }
    markers.value = [];
}

onMounted(() => {
    const mapContainer = document.getElementById('map')
    const mapOption = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567), // 서울 중심
        level: 3,
    }
    map = new kakao.maps.Map(mapContainer, mapOption)
    infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })

    keyword.value = '삼성화재 유성 연수원'
    console.log(keyword.value)

    searchPlaces(keyword.value)
})

watch(() => props.searchParams, (newParams) => {
    if (newParams.city && newParams.district && newParams.bank) {
        keyword.value = `${newParams.city} ${newParams.district} ${newParams.bank}`
        searchPlaces(keyword.value)
    }
}, { deep: true })
</script>

<style scoped>
#map {
    width: 100%;
    height: 400px;
}
</style>
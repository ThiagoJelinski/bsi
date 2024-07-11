const app = Vue.createApp({
    data() {
        return {
            product: 'Socks',
            image: './assets/images/socks_green.jpg',
            inventory: 0,
            onSale: true,
            url: 'https://github.com/csp1po/intro_vue_3/tree/t3-start'
        }
    }
})
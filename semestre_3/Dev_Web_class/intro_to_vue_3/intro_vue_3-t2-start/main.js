const app = Vue.createApp({
    data() {
        return {
            product: 'Socks',
            image: './assets/images/socks_green.jpg',
            inventory: 5,
            onSale: true,
            details: ['50% cotton', '30% wool', '20% polyester'],
            variants: [
                { id: 2234, color: 'green' },
                { id: 2235, color: 'blue' },
            ],
            sizes: ['S','M','L','XL'],
            url: 'https://github.com/csp1po/intro_vue_3/tree/t3-start'
        }
    }
})
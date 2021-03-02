<template>
    <nav>
        <label class="logo">{{ title }}</label>
        <ul>
            <li><a href="#">Pick</a></li>
            <li><a href="#">View</a></li>
            <li><a href="#">Put</a></li>
        </ul>
    </nav>
</template>

<script>
export default {
    name: "Navbar",
    props: {
        title: {
            type: String,
            default: "You need to pass the title",
        },
    },
}
</script>

<style scoped>
    nav {
        width: 100%;
        height: 50px;
        color: white;
    }
    ul {
        float: right;
        margin-right: 50px;
        list-style: none;
        box-sizing: border-box;
        padding: 0;
        margin-right: 80px;
    }
    li {
        display: inline-block;
        line-height: 20px;
        margin: 0 10px;
    }
    a {
        color: white;
        font-size: 20px;
        padding: 5px 7px;
        border-radius: 3px;
        text-transform: capitalize;
        text-decoration: none;
    }
    a:hover {
        background: white;
        color: black;
        transition: .5s;
    }
    .logo {
        color: white;
        font-size: 40px;
        padding: 5%;
    }
</style>
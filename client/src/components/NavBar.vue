<template>
    <header class="header" id="header">
        <nav class="nav container">
            <div class="nav__logo">
                <i class="ri-cash-line nav__logo-icon"></i>
                <a href="#" class="nav__logo-label">Payback</a>
            </div>


            <div class="nav__menu" id="nav-menu">
                <ul class="nav__list">
                    <li class="nav__item">
                        <router-link to="/" class="nav__link">Home</router-link>
                    </li>
                    <li class="nav__item">
                        <router-link to="/form" class="nav__link">Form</router-link>
                    </li>
                    <li class="nav__item">
                        <router-link to="/history" class="nav__link">History</router-link>
                    </li>
                </ul>
            </div>
            <div class="nav__actions">
                <!-- Sign Up -->
                <!-- <a href="" class="nav__register">Sign In</a> -->
                <!-- Log In -->
                <!-- <a href="" class="nav__logi n">Log In</a> -->
            </div>
        </nav>
    </header>
</template>

<script>

</script>

<style>
/*=============== HEADER & NAV ===============*/
.header {
    position: fixed;
    width: 100%;
    top: 0;
    left: 0;
    background-color: var(--white-color);
    z-index: var(--z-fixed);
    transition: background-color .4s, box-shadow .4s;
    border-bottom: 1px solid var(--text-color-lightest);
}

.nav {
    position: relative;
    height: var(--header-height);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: var(--small-font-size);
    font-weight: var(--font-semi-bold);
    padding-bottom: 2em;
    padding-top: 2rem;
}

.nav__logo {
    display: flex;
    align-items: center;
    column-gap: 0.75rem;
    transition: color .4s;
    font-size: var(--h3-font-size);
}

.nav__logo-icon {
    color: var(--first-color-alt);
}

.nav__logo-label {
    color: var(--title-color)
}

.nav__menu {
    margin-right: auto;
    margin-left: 2rem;
}

.nav__list {
    display: flex;
    flex-direction: row;
    column-gap: 1.25rem;
    text-align: center;
}

.nav__link {
    color: var(--text-color-light);
    transition: color .4s;
}

.nav__link:hover {
    color: var(--first-color);
}

.nav__register,
.nav__login {
    display: inline-flex;
    align-items: center;
    /* font-size: 1.25rem; */
    cursor: pointer;
}

.nav__actions {
    display: flex;
    column-gap: 1.25rem;
}

.nav__register {
    color: var(--title-color);
    /* color: var(--white-color); */
}

.nav__login {
    color: var(--white-color);
    background-color: var(--first-color-light);
    padding: .75rem 1rem;
    border-radius: 10px;
}
</style>

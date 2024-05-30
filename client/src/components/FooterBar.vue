<template>
    <!-- FOOTER -->
    <footer class="footer">
        <div class="footer__container container grid">
            <div class="footer__content grid">
                <a href="http://localhost:8080/form" class="footer__logo">Payback</a>
            </div>
        </div>
    </footer>
</template>

<style>
/*=============== FOOTER ===============*/
.footer {
    background-color: var(--first-color);
}

.footer__container {
    padding-block: 4rem 2rem;
    text-align: center;
    row-gap: 5rem;
}

.footer__content {
    row-gap: 2rem;
}

.footer__content a,
.footer__copy {
    color: var(--white-color);
}
</style>
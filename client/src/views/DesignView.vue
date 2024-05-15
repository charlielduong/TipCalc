<template>
    <div class="design">

        <section class="form section">
            <div class="form__container container grid">
                <form action="" class="form__main grid" id="main-form">
                    <div class="form__screen">
                        <div class="form__screen-menu">

                        </div>
                    </div>

                    <div class="form__receipt grid">
                        <h1 class="form__receipt-logo">Receipt</h1>
                        <ul class="form__receipt-items"></ul>
                        <div class="form__receipt-totals"></div>

                    </div>
                </form>
            </div>
        </section>
    </div>
</template>

<script>
export default {
    name: 'DesignView',
}
</script>

<style>
/* Acts as a "main" */
.design {
    overflow: hidden;
}

.form__container {
    background-color: var(--container-color);
    padding: 2rem;
    border-radius: 10px;
    border: 0.5px solid var(--text-color-lightest);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    /* display: flex; */
}

.form__main {
    width: 100%;  
    height: 70dvh;
    display: flex;
}

.form__screen {
    background-color: var(--white-color);
    flex: 65%;
    margin: 7% 12%;
    border-radius: 10px;
    border: 0.5px solid var(--text-color-lightest);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}
.form__receipt {
    background-color: var(--white-color);
    flex: 35%;
    border-radius: 10px;
    border: 0.5px solid var(--text-color-lightest);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

/* .form__screen-menu {
    width: 68%;
    height: 69%;
    background-color: var(--white-color);
    border: 0.3px solid var(--text-color-lightest);
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
} */


/* .form__receipt {
    width: 27%;
    height: 90%;
    border-radius: 10px;
    background-color: var(--white-color);
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    margin-right: 2rem;
    display: flex;
    flex-direction: column;
}

.form__receipt-logo {
    font-size: var(--small-font-size);
    padding-top: 2rem;
    padding-bottom: 2rem;
    align-self: center;
    width: 80%;
    text-align: center;
    border-bottom: 1px solid var(--text-color-lightest);
} */
</style>
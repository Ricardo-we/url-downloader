const defaultSelector = ".b-photos__item__img"
const closeButtonClass = ".pswp__button--close";

const getContent = (previous = [], selector = defaultSelector) => {
    const data = Array.from(document.querySelectorAll(selector)).map(element => element?.src)
    const d = new Set([...previous, ...data]);
    return Array.from(d);
}

const getVideosContent = (previous = [], selector = defaultSelector) => {
    const data = []
    Array.from(document.querySelectorAll(selector)).forEach((element) => {
        element?.click();
        const newSrc = document.querySelector("video")?.children[0]?.src;
        data.push(newSrc)
        document.querySelector(closeButtonClass)?.click();
    })

    const d = new Set([...previous, ...data]);
    return Array.from(d);
}

const main = () => {
    let data = [];
    let paused = false;
    const isVideo = confirm("¿Desea recolectar videos?");

    const interval = setInterval(() => {
        if (paused) return;
        window.scrollTo(0, document.body.scrollHeight);
        if (isVideo) data = getVideosContent(data);
        else data = getContent(data);
    }, isVideo ? 2000 : 1300);

    const stopInterval = setInterval(() => {
        paused = !confirm("¿Desea continuar?");

        if (paused) {
            clearInterval(interval);
            clearInterval(stopInterval);
            // interval.refresh()
            console.log(JSON.stringify(data, null, 4));
        }
    }, 6000);

}

main();
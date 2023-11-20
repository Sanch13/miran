function printImage() {
    const imageSrc = document.getElementById("printableImage").src;
    const imageSize = "width='100' height='100'";
    const imageStyles = "style='position: absolute; top: 0; left: 0;'";

    const printWindow = window.open('', '_blank');
    const printDocument = `
            <!DOCTYPE html>
            <html lang="">
            <head>
            </head>
            <body>
                <img src="${imageSrc}" ${imageSize} ${imageStyles}  alt=""/>
            </body>
            </html>
        `;

    printWindow.document.write(printDocument);
    printWindow.document.close();

    printWindow.onload = function () {
        printWindow.print();
        printWindow.close();
    };
}

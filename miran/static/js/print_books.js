function printBook() {
        const printContent = document.getElementById("printQR").innerHTML;

        const printWindow = window.open('', '_blank');
        const printDocument = `
                    <!DOCTYPE html>
                    <html lang="">
                    <head>
                    </head>
                    <body>
                        ${printContent}
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

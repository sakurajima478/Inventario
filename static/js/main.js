const alertCloseButton = document.querySelector('.alert-button');

alertCloseButton.addEventListener('click', () => {
    const alertElement = document.querySelector('.alert');
    alertElement.style.display = 'none';
});

function openNav() {
    document.getElementById("mobile-menu").style.width = "100%";
}

function closeNav() {
    document.getElementById("mobile-menu").style.width = "0%";
}


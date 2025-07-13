document.addEventListener('DOMContentLoaded', () => {
  for (let i = 0; i < 30; i++) {
    const cross = document.createElement('div');
    cross.className = 'cross';
    cross.textContent = '†'; // Você pode usar outro caractere gótico aqui

    // Posição horizontal aleatória
    cross.style.left = Math.random() * 100 + 'vw';

    // Duração aleatória da animação
    cross.style.animationDuration = (2 + Math.random() * 3) + 's';

    document.body.appendChild(cross);
  }
});
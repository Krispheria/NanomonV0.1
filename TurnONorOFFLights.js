<script>
    function encenderLed() {
      fetch('http://192.168.43.212:80/encender', { method: 'POST' })
        .then(response => {
          if (response.ok) {
            return response.text();
          }
          throw new Error('Error al encender el LED');
        })
        .then(data => {
          actualizarEstado(data); // Actualizar el estado después de encender el LED
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }

    function apagarLed() {
      fetch('http://192.168.43.212:80/apagar', { method: 'POST' })
        .then(response => {
          if (response.ok) {
            return response.text();
          }
          throw new Error('Error al apagar el LED');
        })
        .then(data => {
          actualizarEstado(data); // Actualizar el estado después de apagar el LED
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }
</script>

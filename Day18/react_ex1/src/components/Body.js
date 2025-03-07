export default function Body() {
    return (
      <main style={styles.container}>
        <section style={styles.hero}>
          <h2>Welcome to My Website</h2>
          <p>Explore and learn more about us!</p>
          <button style={styles.button}>Get Started</button>
        </section>
  
        <section style={styles.features}>
          <div style={styles.featureBox}>
            <h3>Feature 1</h3>
            <p>Discover amazing services we offer.</p>
          </div>
          <div style={styles.featureBox}>
            <h3>Feature 2</h3>
            <p>Expand your knowledge with our resources.</p>
          </div>
          <div style={styles.featureBox}>
            <h3>Feature 3</h3>
            <p>Stay updated with the latest trends.</p>
          </div>
        </section>
      </main>
    );
  }
  
  const styles = {
    container: {
      padding: "20px",
      fontFamily: "Arial, sans-serif",
      textAlign: "center",
    },
    hero: {
      backgroundColor: "#4CAF50",
      color: "white",
      padding: "50px 20px",
      borderRadius: "10px",
      marginBottom: "20px",
    },
    button: {
      backgroundColor: "white",
      color: "#4CAF50",
      border: "none",
      padding: "10px 20px",
      fontSize: "16px",
      cursor: "pointer",
      borderRadius: "5px",
      marginTop: "10px",
    },
    features: {
      display: "flex",
      justifyContent: "space-around",
      gap: "15px",
      flexWrap: "wrap",
    },
    featureBox: {
      backgroundColor: "#f4f4f4",
      padding: "20px",
      borderRadius: "8px",
      width: "30%",
      minWidth: "200px",
      boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
    },
  };
  
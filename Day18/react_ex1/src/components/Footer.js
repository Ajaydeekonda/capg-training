export default function Footer() {
    return (
      <footer style={styles.footer}>
        <p>&copy; {new Date().getFullYear()} My Website. All Rights Reserved.</p>
        <div style={styles.socialLinks}>
          <a href="#" style={styles.link}>Facebook</a>
          <a href="#" style={styles.link}>Twitter</a>
          <a href="#" style={styles.link}>Instagram</a>
        </div>
      </footer>
    );
  }
  
  const styles = {
    footer: {
      backgroundColor: "#333",
      color: "white",
      textAlign: "center",
      padding: "15px 0",
      marginTop: "20px",
    },
    socialLinks: {
      marginTop: "10px",
    },
    link: {
      color: "white",
      textDecoration: "none",
      margin: "0 10px",
    },
  };
  
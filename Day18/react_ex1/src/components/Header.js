export default function Header() {
  return (
    <header style={styles.header}>
      <h1 style={styles.logo}>My Website</h1>
      <nav>
        <ul style={styles.navList}>
          <li style={styles.navItem}>
            <a href="#" style={styles.navLink}>
              Home
            </a>
          </li>
          <li style={styles.navItem}>
            <a href="#" style={styles.navLink}>
              About
            </a>
          </li>
          <li style={styles.navItem}>
            <a href="#" style={styles.navLink}>
              Contact
            </a>
          </li>
        </ul>
      </nav>
    </header>
  );
}

const styles = {
  header: {
    backgroundColor: "#333",
    color: "white",
    padding: "15px 20px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  logo: {
    fontSize: "24px",
    margin: 0,
  },
  navList: {
    listStyle: "none",
    padding: 0,
    display: "flex",
    gap: "20px",
  },
  navItem: {
    fontSize: "18px",
  },
  navLink: {
    color: "white",
    textDecoration: "none",
    transition: "color 0.3s",
  },
};

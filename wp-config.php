<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'root');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '.h~+k`9&*7z>vC7)F*q.F9lI$CPVN.$u=a,ARcmwqQc|M^h,S#RC4gkRAi6}81W;');
define('SECURE_AUTH_KEY',  'k |?K-k[XQgDGMM[)mQbUhoLONF@EuK^?ch,_o)If(,cPdlZy*DdHU176JLZ*Z3|');
define('LOGGED_IN_KEY',    'tngj|g.|+c5k42R?js8m0swtf#A@y[*N=.*@3R3,Aa-}q6A/+Q9Y_8%XumRhu`jj');
define('NONCE_KEY',        'y[9.qx?C9qqqy,_zj<2R&w}XNDkjWf!2LdFmi%|AkT-?/xAp{JxUwJ OD}$r~S8G');
define('AUTH_SALT',        'VidoQ{>90 O62q:N2bLr08o7dc(+(40+gRDh;oq!?~z:x:P_@z )1}Xt8_|wWUX5');
define('SECURE_AUTH_SALT', 'hy3Ea[?`H4usrxN4lE+zlP!x7;6fo;-Qv]DwlaJ~r>u%|]e*1#jsU,YT3*BG!q)z');
define('LOGGED_IN_SALT',   'avJOxa8AU:_A%b0x.<|3I;pZK_l/x4$A8Zxr+t[Tq6ij[JrK$[Y>_JD,JRZ!1*~|');
define('NONCE_SALT',       'NU$VD/]?R2|H P. &F=NFjy7Bqs[`yS;NMGWFd##6!>YBCjp >,Ig.td5I54-3F ');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');

plugins { id("com.android.application") }
android {
    namespace = "app.eversage.offline"
    compileSdk = 35
    defaultConfig {
        applicationId = "app.eversage.offline"
        minSdk = 26
        targetSdk = 35
        versionCode = 3
        versionName = "0.3.0"
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
}

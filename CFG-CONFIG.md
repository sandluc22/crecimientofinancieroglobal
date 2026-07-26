# ⚙️ CFG — Configuración del proyecto

**Proyecto:** crecimientofinancieroglobal.com  
**Última actualización:** 10 julio 2026

---

## 🌐 Infraestructura

| Elemento | Estado | Notas |
|----------|--------|-------|
| **Hosting** | Surge | crecimientofinancieroglobal.surge.sh |
| **CDN/Proxy** | Cloudflare activo | Proxy ON, SSL Full |
| **SSL** | ✅ Funcionando | Cloudflare gestiona SSL |
| **Dominio** | crecimientofinancieroglobal.com | DNS en Surge + Cloudflare |
| **Analytics** | ❌ No verificado | Pendiente confirmar si está recibiendo datos |
| **Search Console** | ❌ No verificado | Pendiente confirmar si dominio está verificado y sitemap enviado |

---

## 📦 Código

| Elemento | Ruta | Estado |
|----------|------|--------|
| **Versión original (azul+amarillo)** | `crecimientofinancieroglobal.com/index.html` | ✅ Guardada |
| **Versión naranja con formulario** | `netlify-deploy/index.html` | ✅ Lista para desplegar |
| **Backup 28 junio** | `backup-web-28jun-seguro/` | ✅ |
| **Backup 5 julio** | `backup-web-05jul-oscura-completo.tar.gz` | ✅ |
| **Deploy Netlify** | crecimientofinancierogloba.netlify.app | ⚠️ Subido pero dominio no apunta aquí |

---

## 🎯 Tareas pendientes

### Prioridad 1 — Urgente
- [ ] **Desplegar el naranja + formulario** — El index.html con naranja quemado, desplegable aseguradoras (10 opciones), fecha nacimiento y captcha está listo en `/home/node/netlify-deploy/`. El dominio apunta a **Surge** y no podemos hacer login (contraseña no válida).    
  **Soluciones posibles:**
  - Resetear contraseña de Surge (desde surge.sh o por email)
  - Page Rule en Cloudflare que redirija a Netlify
  - Token de API de Cloudflare para poder hacer la Page Rule desde aquí

### Prioridad 2 — Validación
- [ ] **Probar envío del formulario** — Confirmar que con el captcha activado no sale el mensaje de "lugar no seguro"
- [ ] **Verificar Search Console** — Comprobar que el dominio está verificado y el sitemap se ha enviado correctamente
- [ ] **Indexar subpáginas en Google** — Asegurar que Google tiene todas las páginas indexadas

### Prioridad 3 — Mantenimiento
- [ ] **Subir backup a Netlify** — Ya está subida la versión naranja, pero tener la versión actual como backup extra
- [ ] **Guardar credenciales de Cloudflare** — API Token o Global API Key para poder gestionar desde aquí
- [ ] **Actualizar backups** — Tener siempre una copia reciente del código desplegado

---

## 🔑 Credenciales

Ver `/home/node/workspace/CLAVES.md`

- Surge: crecimientofinancieroglobal@gmail.com / contraseña no válida (pendiente reset)
- Netlify: Token `nfp_SwA8eHye3jrJn2siYEnmPKvjtTi5fiEDf3eb` (⚠️ da "Access Denied" en API — pendiente regenerar con permisos)
- Cloudflare: crecimientofinancieroglobal@gmail.com / AlfaySandra.1 (sin API Key guardada)
- Gmail: crecimientofinancieroglobal@gmail.com / AlfaySandra.1

---

## 📝 Historial de cambios

| Fecha | Cambio |
|-------|--------|
| 5 jul 2026 | Configuración inicial: Cloudflare, SSL, Analytics, Search Console |
| 5 jul 2026 | 6 artículos blog, sitemap generado |
| 10 jul 2026 | Cambio color amarillo → naranja quemado (`#d4560a`) |
| 10 jul 2026 | Formulario: fecha nacimiento + desplegable aseguradoras + captcha |
| 10 jul 2026 | Deploy a Netlify (pendiente servir desde dominio) |

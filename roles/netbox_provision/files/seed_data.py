from dcim.models import Site
from ipam.models import Prefix

# 1. Gestion du Site
site_name = "IUT Roanne"
site_slug = "iut-roanne"

site, _ = Site.objects.get_or_create(
    slug=site_slug,
    defaults={'name': site_name, 'status': 'active'}
)
print(f"ℹ️ Site '{site.name}' (ID: {site.pk}) est prêt.")

# 2. Gestion du Préfixe IP (Méthode blindée)
prefix_val = "192.168.10.0/24"

if not Prefix.objects.filter(prefix=prefix_val).exists():
    try:
        # ÉTAPE A : Création NEUTRE (sans lier au site pour éviter l'erreur)
        prefix = Prefix(prefix=prefix_val, status='active')
        prefix.save()
        print(f"✅ Préfixe '{prefix_val}' créé avec succès.")

        # ÉTAPE B : Tentative de liaison via l'ID brut (contourne le bug d'assignation)
        try:
            prefix.site_id = site.pk
            prefix.save()
            print(f"✅ Préfixe lié au site '{site_name}'.")
        except Exception as e:
            print(f"⚠️ Préfixe créé, mais liaison site ignorée (Bug API): {e}")

    except Exception as global_e:
        print(f"❌ Erreur critique création préfixe: {global_e}")
else:
    print(f"ℹ️ Le préfixe '{prefix_val}' existe déjà.")

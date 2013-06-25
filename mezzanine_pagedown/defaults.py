from mezzanine.conf import register_setting

register_setting(
    name="PAGEDOWN_SERVER_SIDE_PREVIEW",
    description="Generate previews of the rendered HTML on the server using ajax requests.",
    editable=False,
    default=False,
)

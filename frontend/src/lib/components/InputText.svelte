<script lang="ts">
	export let label: string | null = null;
	export let placeholder: string | null = label;
	export let value: string | null = null;
</script>

<label class="flex flex-col"
	>{label ? label + ":" : ""}
	<input bind:value type="text" {placeholder} class="border-2 p-1 rounded-md" />
</label>

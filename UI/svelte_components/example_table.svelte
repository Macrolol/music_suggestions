<script>
	import SvelteTable from 'svelte-table';
	import { data } from './myLittleData.js.js'
	const rows = data;
	
	// define column configs
	const columns = [
		{
			key: "number",
			title: "Number",
			value: v => v.number,
			sortable: true,
			filterOptions: rows => {
				// generate groupings of 0-10, 10-20 etc...
				let nums = {};
				rows.forEach(row => {
					if (typeof row.number === 'string') {
						let v = row.number.charAt(0)
						nums[v] = { name: v, value: v};
					} else {
						let num = Math.floor(row.number / 10);
						if (nums[num] === undefined) {
							nums[num] = { name: `${num * 10} to ${(num + 1) * 10}`, value: num };
						}
					}
				});
				// fix order
				nums = Object.entries(nums)
					.sort()
					.reduce((o, [k, v]) => ((o[k] = v), o), {});
				return Object.values(nums);
			},
			filterValue: v => {
				if (typeof v.number === 'string') {
					return v.number.charAt(0);
				}
				return Math.floor(v.number / 10);
			},
		},
		{
			key: "episode",
			title: "Episode",
			value: v => v.episode,
			sortable: true,
		},
		{
			key: "season",
			title: "Season",
			value: v => v.season,
			filterOptions: rows => {
				let nums = {};
				rows.forEach(row => {
					let num = row.season;
					if (nums[num] === undefined)
						nums[num] = {name: num, value: num};
				});
				// fix order
				nums = Object.entries(nums)
					.sort()
					.reduce((o, [k, v]) => ((o[k] = v), o), {});
				return Object.values(nums);
			},
			filterValue: v => v.season,
			sortable: true,
		},
		{
			key: "title",
			title: "Title",
			value: v => v.title,
			sortable: true,
			filterOptions: rows => {
				// use first letter of first_name to generate filter
				let letrs = {};
				rows.forEach(row => {
					let letr = row.title.charAt(0);
					if (letrs[letr] === undefined)
						letrs[letr] = {
							name: `${letr.toUpperCase()}`,
							value: letr.toLowerCase()
						};
				});
				// fix order
				letrs = Object.entries(letrs)
					.sort()
					.reduce((o, [k, v]) => ((o[k] = v), o), {});
				return Object.values(letrs);
			},
			filterValue: v => v.title.charAt(0).toLowerCase()
		},
	];
</script>

<SvelteTable columns="{columns}" rows="{rows}"></SvelteTable>
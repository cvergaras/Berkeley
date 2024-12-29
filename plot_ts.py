#%%P
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import os
#%%
# Open the NetCDF file
ds = nc.Dataset(os.path.join('output','output.nc'))

# Get time data and convert to datetime objects
time = ds.variables['time'][:]
start_date = datetime.strptime("1991-05-01 00:00:00", '%Y-%m-%d %H:%M:%S')
dates = []
for t in time:
    date = start_date + timedelta(days=t/24)
    dates.append(date)
# dates = [start_date + timedelta(days=t/24) for t in time]
#%%
print(dates)
#%%
# Get depth data
z = ds.variables['z'][0, :, 0, 0].compressed()  # Get depths for first time step
#%%
print(len(z))

#%%
# Select some depths to plot (e.g., every 50th depth level)
depth_indices = np.arange(0, len(z), 50)
selected_depths = z[depth_indices]

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
#%%
# Plot temperature
for idx in depth_indices:
    temp = ds.variables['temp'][:, idx, 0, 0]
    ax1.plot(dates, temp, label=f'Depth: {z[idx]:.1f} m')

ax1.set_title('Temperature Time Series at Different Depths')
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)')
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax1.grid(True)

# Plot salinity
for idx in depth_indices:
    salt = ds.variables['salt'][:, idx, 0, 0]
    ax2.plot(dates, salt, label=f'Depth: {z[idx]:.1f} m')

ax2.set_title('Salinity Time Series at Different Depths')
ax2.set_xlabel('Date')
ax2.set_ylabel('Salinity')
ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
print("plot")
# Save the figure
plt.savefig('lake_temp_salt_profiles.png', bbox_inches='tight', dpi=300)

# Close the dataset
ds.close()

plt.show()
#%%
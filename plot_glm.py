# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.colors as mcolors
# import myfunctions
# import os
# import netCDF4 as nc

# glm_workspace_new = os.path.join("GLMmodel", "GLM3.3Kepwari_RENA_t2_geo")
# out_folder = os.path.join(glm_workspace_new, "Output")

# Data_GLM = nc.Dataset(os.path.join(out_folder,"output.nc")) #reading output from GLM
# print(Data_GLM)

# depth = Data_GLM.variables['z'][:,:,0,0]#.compressed() ## [time,z,lat,long]
# time = [x for x in range(depth.shape[0])]
# data =  Data_GLM.variables['salt'][:,:,0,0]



# lake_levels = []
# for i in range(len(time)):
#     max_depth = depth[i].max()
#     lake_levels.append(max_depth)


# def plot_glm(time, depth, data, lake_levels):
#     fig, ax = plt.subplots(figsize=(10, 6))
    
#     # Create discrete bounds for the colormap
#     bounds = np.linspace(data.min(), data.max(), num=10)
#     norm = mcolors.BoundaryNorm(boundaries=bounds, ncolors=256)
    
#     # Plot the data with discrete colormap
#     c = ax.pcolormesh(time, depth, data, cmap='viridis', norm=norm, shading='auto')
    
#     # Add a colorbar with discrete ticks
#     cbar = fig.colorbar(c, ax=ax, boundaries=bounds, ticks=bounds)
#     cbar.set_label('Temperature (°C)')
    
#     # Mask data above lake level
#     for i in range(len(time)):
#         lake_level = lake_levels[i]
#         depth_mask = depth >= lake_level
#         data_mask = np.ma.masked_where(depth_mask, data[:, i])
#         ax.pcolormesh([time[i], time[i+1]], depth, data_mask, cmap='viridis', norm=norm, shading='auto')
    
#     ax.set_xlabel('Time')
#     ax.set_ylabel('Elevation (m)')
#     ax.set_title('Seasonal Temperature Variation in Lake')
#     ax.invert_yaxis()  # Invert y-axis to have the surface at the top
#     plt.show()

# plot_glm(time, depth, data, lake_levels)

# import os
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
# import netCDF4 as nc

# def plot_glm_results(output_folder):
#     # Load the data from the NetCDF file
#     Data_GLM = nc.Dataset(os.path.join(output_folder, "output.nc"))

#     # Extract the necessary variables
#     time = np.arange(Data_GLM.variables['salt'].shape[0])
#     salt = Data_GLM.variables['salt'][:, :, 0, 0]
#     trc_tr1 = Data_GLM.variables['TRC_tr1'][:, :, 0, 0]
#     trc_tr2 = Data_GLM.variables['TRC_tr2'][:, :, 0, 0]

#     # Prepare depths array
#     depths_list = [Data_GLM.variables['z'][t, :, 0, 0] for t in range(len(time))]

#     # Set up the plot
#     fig, axes = plt.subplots(3, 1, figsize=(10, 18), dpi=300)
#     cmap = 'viridis'

#     def plot_variable(ax, time, depths, variable, title, label, cmap):
#         norm = mcolors.BoundaryNorm(boundaries=np.linspace(np.nanmin(variable), np.nanmax(variable), num=11), ncolors=256)
#         for t in range(len(time)):
#             depth = depths[t]
#             var = variable[t]
#             ax.plot(time[t] * np.ones(len(depth)), depth, 'k-', lw=0.5)
#             img = ax.scatter(time[t] * np.ones(len(depth)), depth, c=var, cmap=cmap, norm=norm, s=5)
#         fig.colorbar(img, ax=ax, label=label)
#         ax.set_title(title)
#         ax.set_ylabel('Depth (m)')
#         ax.invert_yaxis()

#     # Plot the salt concentration
#     plot_variable(axes[0], time, depths_list, salt, 'Salt Concentration', 'Salt concentration', cmap)

# #     # Plot the TRC_tr1 concentration
# #     plot_variable(axes[1], time, depths_list, trc_tr1, 'TRC_tr1 Concentration', 'TRC_tr1 concentration', cmap)

# #     # Plot the TRC_tr2 concentration
# #     plot_variable(axes[2], time, depths_list, trc_tr2, 'TRC_tr2 Concentration', 'TRC_tr2 concentration', cmap)

# #     axes[2].set_xlabel('Time')

# #     plt.tight_layout()
# #     plt.show()

# # # Usage
# # output_folder = "GLMmodel/GLM3.3Kepwari_RENA_t2_v2/Output"
# # plot_glm_results(output_folder)

# import os
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
# import netCDF4 as nc

# def plot_glm_results(output_folder):
#     # Load the data from the NetCDF file
#     Data_GLM = nc.Dataset(os.path.join(output_folder, "output.nc"))

#     # Extract the necessary variables
#     time = np.arange(Data_GLM.variables['salt'].shape[0])
#     salt = Data_GLM.variables['salt'][:, :, 0, 0]
#     trc_tr1 = Data_GLM.variables['OXY_oxy'][:, :, 0, 0]
#     trc_tr2 = Data_GLM.variables['CAR_pH'][:, :, 0, 0]

#     # Prepare depths array
#     depths_list = [Data_GLM.variables['z'][t, :, 0, 0] for t in range(len(time))]

#     # Set up the plot
#     fig, axes = plt.subplots(3, 1, figsize=(10, 18), dpi=300)
#     cmap = 'viridis'

#     def plot_variable(ax, time, depths, variable, title, label, cmap):
#         norm = mcolors.BoundaryNorm(boundaries=np.linspace(np.nanmin(variable), np.nanmax(variable), num=11), ncolors=256)
#         for t in range(len(time)):
#             depth = depths[t]
#             var = variable[t]
#             # ax.plot(time[t] * np.ones(len(depth)), depth, 'k', lw=0.5)
#             img = ax.scatter(time[t] * np.ones(len(depth)), depth, c=var, cmap=cmap, norm=norm, s=60, marker = 's')
#         ax.axhline(y=0, color='k', linestyle='-', lw=3)
#         fig.colorbar(img, ax=ax, label=label)
#         ax.set_title(title)
#         ax.set_ylabel('Depth (m)')
#         # ax.invert_yaxis()  # Invert the vertical axis

#     # Plot the salt concentration
#     plot_variable(axes[0], time, depths_list, salt, 'Salt Concentration', 'Salt concentration', cmap)

#     # Plot the TRC_tr1 concentration
#     plot_variable(axes[1], time, depths_list, trc_tr1, 'TRC_tr1 Concentration', 'TRC_tr1 concentration', cmap)

#     # Plot the TRC_tr2 concentration
#     plot_variable(axes[2], time, depths_list, trc_tr2, 'TRC_tr2 Concentration', 'TRC_tr2 concentration', cmap)

#     axes[2].set_xlabel('Time')

#     plt.tight_layout()
#     plt.show()

# # Usage
# import netCDF4 as nc
# glm_workspace_new = os.path.join("GLMmodel", "GLM3.3Kepwari_RENA_t2_geo")
# out_folder = os.path.join(glm_workspace_new, "Output")
# Data_GLM = nc.Dataset(os.path.join(out_folder, "output.nc"))


# # Extract the necessary variables

# ph = Data_GLM.variables['CAR_pH'][:, :, 0, 0]
# ph[-1]

# #%%
# plot_glm_results(out_folder)


# import os
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
# import netCDF4 as nc

# def plot_glm_results(output_folder):
#     # Load the data from the NetCDF file
#     Data_GLM = nc.Dataset(os.path.join(output_folder, "output.nc"))

#     # Extract the necessary variables
#     time = np.arange(Data_GLM.variables['salt'].shape[0])
#     salt = Data_GLM.variables['salt'][:, :, 0, 0]
#     trc_tr1 = Data_GLM.variables['TRC_tr1'][:, :, 0, 0]
#     trc_tr2 = Data_GLM.variables['TRC_tr2'][:, :, 0, 0]

#     # Prepare depths array
#     depths_list = [Data_GLM.variables['z'][t, :, 0, 0] for t in range(len(time))]

#     # Set up the plot
#     fig, axes = plt.subplots(3, 1, figsize=(10, 18), dpi=300)
#     cmap = 'viridis'

#     def plot_variable(ax, time, depths, variable, title, label, cmap):
#         norm = mcolors.BoundaryNorm(boundaries=np.linspace(np.nanmin(variable), np.nanmax(variable), num=11), ncolors=256)
#         for t in range(len(time)):
#             depth = depths[t]
#             var = variable[t]
#             ax.plot(time[t] * np.ones(len(depth)), depth, 'k-', lw=0.5)
#             img = ax.scatter(time[t] * np.ones(len(depth)), depth, c=var, cmap=cmap, norm=norm, s=5)
#         fig.colorbar(img, ax=ax, label=label)
#         ax.set_title(title)
#         ax.set_ylabel('Depth (m)')
#         ax.invert_yaxis()

#     # Plot the salt concentration
#     plot_variable(axes[0], time, depths_list, salt, 'Salt Concentration', 'Salt concentration', cmap)

#     # Plot the TRC_tr1 concentration
#     plot_variable(axes[1], time, depths_list, trc_tr1, 'TRC_tr1 Concentration', 'TRC_tr1 concentration', cmap)

#     # Plot the TRC_tr2 concentration
#     plot_variable(axes[2], time, depths_list, trc_tr2, 'TRC_tr2 Concentration', 'TRC_tr2 concentration', cmap)

#     axes[2].set_xlabel('Time')

#     plt.tight_layout()
#     plt.show()

# # Usage
# output_folder = "GLMmodel/GLM3.3Kepwari_RENA_t2_v2/Output"
# plot_glm_results(output_folder)

#%%
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import netCDF4 as nc

def plot_glm_results(output_folder, var):
    # Load the data from the NetCDF file
    # output_folder = "GLMmodel/GLM3.3Kepwari_RENA_t2_geo_test2/Output"
    Data_GLM = nc.Dataset(os.path.join(output_folder, "output.nc"))

    # Extract the necessary variables
    # var = "salt"
    time = np.arange(Data_GLM.variables[var].shape[0])
    # print(time)
    salt = Data_GLM.variables[var][:, :, 0, 0]
    salt.min()
    # trc_tr1 = Data_GLM.variables['GEO_FeII'][:, :, 0, 0]
    # trc_tr2 = Data_GLM.variables['GEO_FeIII'][:, :, 0, 0]
    # print(trc_tr1[0])
    # Prepare depths array
    depths_list = [Data_GLM.variables['z'][t, :, 0, 0] for t in range(len(time))]

    # Set up the plot
    fig, axes = plt.subplots(3, 1, figsize=(5, 9), dpi=300)
    cmap = 'viridis'

    def plot_variable(ax, time, depths, variable, title, label, cmap):
        # norm = mcolors.BoundaryNorm(boundaries=np.linspace(np.nanmin(variable), np.nanmax(variable), num=11), ncolors=256)
        for t in range(len(time)):
            depth = depths[t]
            var1 = variable[t]
            # ax.plot(time[t] * np.ones(len(depth)), depth, 'k', lw=0.5)
            # if title == 'Fe(II)':
            #     vmin = 0
            #     vmax = 0.013
            #     img = ax.scatter(time[t] * np.ones(len(depth)), depth, c=var1/1300, cmap=cmap, s=60, marker = 's',vmin=vmin, vmax=vmax)
            # elif title == 'Fe(III)':
            #     vmin = 0
            #     vmax = 0.0013
            #     img = ax.scatter(time[t] * np.ones(len(depth)), depth, c=var1/300, cmap=cmap, s=60, marker = 's',vmin=vmin, vmax=vmax)
            # else:
            vmin = variable.min()
            vmax = variable.max()#8.0
            img = ax.scatter(time[t] * np.ones(len(depth)), depth, c=var1, cmap=cmap, s=60, marker = 's',vmin=vmin, vmax=vmax)
        ax.axhline(y=0, color='white', linestyle='-', lw=3)
        fig.colorbar(img, ax=ax, label=label)
        ax.set_title(title)
        ax.set_ylabel('Depth (m)')
        # ax.set_xlim(0,300)
        # ax.set_ylim(0,60)
        # ax.invert_yaxis()  # Invert the vertical axis

    # Plot the salt concentration
    plot_variable(axes[0], time, depths_list, salt, var, var, cmap)

    # Plot the TRC_tr1 concentration
    # plot_variable(axes[1], time, depths_list, trc_tr1, 'Fe(II)', 'Fe(II) concentration', cmap)

    # # Plot the TRC_tr2 concentration
    # plot_variable(axes[2], time, depths_list, trc_tr2, 'Fe(III)', 'Fe(III) concentration', cmap)

    axes[2].set_xlabel('Time')

    plt.tight_layout()
    plt.show()

#%%
# Usage
# import netCDF4 as nc
output_folder = "output"
# plot_glm_results(output_folder)
Data_GLM = nc.Dataset(os.path.join(output_folder, "output.nc"))


# # # Extract the necessary variables




#%%
plot_glm_results(output_folder,"PHQ_CO_Fe_di")

#%%
ph = Data_GLM.variables["PHQ_CO_Fe_di"][:, :, 0, 0]
ph[0]
ph[0]
# %%

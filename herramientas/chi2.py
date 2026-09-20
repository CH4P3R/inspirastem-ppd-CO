import numpy as np




#Inputs: wavelength, (start, stop, step), 




class chi_min:
	
	def __init__(self, ):
		self._

st_wav = ((vel/(const.c.value*1e-3))+1)*COw[i] # Stacked Profile wavelengths x-axis
        model_mask=(min(st_wav)<(sub_spec.spectral_axis.value))&(sub_spec.spectral_axis.value<max(st_wav))
        
		resam_ = np.interp(wvp[model_mask], st_wav, yfitt-1)
        
        chi_list = []
        scale = np.arange(0.25,1.75,0.01)
        for l in scale:
            chi_2 = np.nansum(   ( (flnp[model_mask]-y_continuum_fitted[model_mask])-(l*resam_) )**2 *
                              (sub_spec_err[model_mask]**(-2)) )
            chi_list.append(chi_2)
        
        scale_min = np.where(min(chi_list)==chi_list)[0][0]
        min_chi = chi_list[scale_min]
        
        best_model = scale[scale_min] * resam_
import specutils
import numpy as np
from astropy.io import fits
from astropy import units as u
from astropy import constants as const
from astropy.nddata import StdDevUncertainty
from specutils import Spectrum1D
from specutils.analysis import line_flux
from specutils import Spectrum1D, SpectralRegion

"""
    Unpacker for incoming fits files

    Parameters
    ----------
    fits_fname : .fits file format
        Raw data containing spectral information. Typically, flux and error is in Jy and wavelength is in nm. 
    stacked_fname : .fits file format
        Stacked line profile (SLP) with four internal 'attributes': velocity [km/s], flux [Jy], flux error [Jy], and averaged flux [Jy]. The flux is the weighted average of most well-behaved lines per disk. 
    
    wavelength = takes incoming nm wavelength and converts to um (micron).
    flux = flux density measurements from data in [Jy]
    fluxd_err = flux density error in [Jy]
    velocity = x-axis of model. Converts km/s -> micron
    fluxm = flux density of the SLP model [Jy]
    fluxm_err = flux density error [Jy]
    fluxam = flux density of the averaged SLP model.
"""


class Unpack:

    def __init__(self, fits_fname , stacked_fname=None):
        self._fitsfile = fits_fname
        if fits_fname is not None:
            specdata = fits.open(fits_fname)[1].data[0]
            fits.open(fits_fname).close()
            self._wavelength = specdata[0] * 1e-3  # micron
            self._fluxd = specdata[1]  # Jy
            self._fluxd_err = specdata[2]  # Jy
        elif fits_fname is None: # trying 'pass'
            pass
        self._stacked_fname = stacked_fname
        # if fits_fname is not None:
        #	print('Great, another .fits data file')
        # if stacked_fname is not None:
        #	print('Oh, look. A stacked line profile.')
        # if fits_fname is None:
        #    continue
        # elif stacked_fname is None:
        #    continue
        if stacked_fname is not None:
            stackdata = fits.open(stacked_fname)[1].data[0]
            fits.open(stacked_fname).close()
            self._velocity = stackdata[0] # km/s
            self._fluxm = stackdata[1] # Jy
            self._fluxm_err = stackdata[2] # Jy
            self._fluxam = stackdata[3] # Jy
        # else:
        #    continue

        self._spec1D = Spectrum1D(flux=self._fluxd * u.Jy, spectral_axis=self._wavelength * u.micron,
                                  uncertainty=StdDevUncertainty(self._fluxd_err, unit='Jy'))

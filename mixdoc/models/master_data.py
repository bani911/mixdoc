# -*- coding: utf-8 -*-

from odoo import models, fields, api

class kalangan_surat(models.Model):
    _name = 'kalangan.surat'

    name = fields.Char(string="Kalangan", required=True)

class jenis_unit(models.Model):
    _name = 'jenis.unit'

    name = fields.Char(string="Jenis Perusahaan", required=True)
    kode = fields.Char(string="Kode", required=True)

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, rec.name + " - " + rec.kode))
        return res

class status_surat(models.Model):
    _name = 'status.surat'

    name = fields.Char(string="Status Surat", required=True)

class jenis_surat(models.Model):
    _name = 'jenis.surat'

    name = fields.Char(string="Nama Surat", required=True)
    kode = fields.Char(string="Kode", required=True)
    ket = fields.Char(string="Keterangan")
    kalangan = fields.Many2one('kalangan.surat', 'Kalangan Surat')

    _sql_constraints = [('cek_unik_name', 'UNIQUE(name)', 'Nama Surat tidak boleh sama!')]

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, rec.name + " - " + rec.kode))
        return res

# class disposisi(models.Model):
#     _name = 'disposisi'
#
#     name = fields.Char(string="Disposisi", required=True)
#     singkatan = fields.Char(string="Singkatan", required=True)
#
#     _sql_constraints = [('cek_unik_name', 'UNIQUE(name)', 'Nama Disposisi tidak boleh sama!')]
#
#     def name_get(self):
#         res = []
#         for rec in self:
#             res.append((rec.id, rec.name + " - " + rec.singkatan))
#         return res

class jenis_dokumen(models.Model):
    _name = 'jenis.dokumen'

    name = fields.Char(string="Jenis Dokumen", required=True)

class bagian(models.Model):
    _name = 'bagian'

    tipe_org = fields.Many2one('jenis.unit', 'Tipe Organisasi', required=True)
    name = fields.Char(string="Bagian", required=True)
    singkatan = fields.Char(string="Singkatan", required=True)

    _sql_constraints = [('cek_unik_name', 'UNIQUE(name)', 'Nama tidak boleh sama!')]

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, rec.name + " - " + rec.singkatan))
        return res

class tempat_simpan(models.Model):
    _name = 'tempat.simpan'

    name = fields.Char(string="Tempat Penyimpanan", required=True)

class disposisi_status_keluar(models.Model):
    _name = 'disposisi.status.keluar'

    name = fields.Char(string="Disposisi Status Surat Keluar", required=True)

class jenis_perusahaan(models.Model):
    _name = 'jenis.perusahaan'

    name = fields.Char(string="Nama", required=True)
    kode = fields.Char(string="Kode", required=True)

    _sql_constraints = [('cek_unik_name', 'UNIQUE(name)', 'Nama Jenis Perusahaan tidak boleh sama!')]

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, rec.name + " - " + rec.kode))
        return res

class kuasa_fisik(models.Model):
    _name = 'kuasa.fisik'

    name = fields.Char(string="Penguasaan Fisik", required=True)

class pengiriman_prosedur(models.Model):
    _name = 'pengiriman.prosedur'

    name = fields.Char(string="Pengiriman Prosedur", required=True)

    _sql_constraints = [('cek_unik_name', 'UNIQUE(name)', 'Nama tidak boleh sama!')]

class gudang(models.Model):
    _name = 'gudang'

    name = fields.Char(string="Gudang", required=True)

class nama_dokumen(models.Model):
    _name = 'nama.dokumen'

    jenis_dokumen = fields.Many2one('jenis.dokumen', 'Jenis Dokumen', required=True)
    name = fields.Char(string="Nama Dokumen", required=True)

    _sql_constraints = [('cek_unik_name', 'UNIQUE(name)', 'Nama tidak boleh sama!')]

class penerima_eksternal(models.Model):
    _name = 'penerima.eksternal'

    name = fields.Char(string="Penerima Eksternal", required=True)

class org_penerima_eksternal(models.Model):
    _name = 'org.penerima.eksternal'

    name = fields.Char(string="Organisasi Penerima Eksternal", required=True)